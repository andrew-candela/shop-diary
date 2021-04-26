#!/bin/bash

prep_deployment_package_in_github_actions () {
    # Prepare the deployment package
    original_wd=`pwd`
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt -q
    pip install . -q
    deactivate
    cd venv/lib/python3.7/site-packages
    zip -r9 ${original_wd}/function.zip .
    cd ${original_wd}

    # Upload the deployment package
    aws s3 cp function.zip s3://${S3_BUCKET}/${ZIP_FILE_KEY}
}

prep_deployment_package () {
    echo "Preparing Deployment Package"
    pip install . -q
    original_wd=`pwd`
    cd ${original_wd}/venv/lib/python3.8/site-packages
    zip --quiet -r9 ${original_wd}/function.zip .
    cd ${original_wd}

    # Upload the deployment package
    aws s3 cp function.zip s3://${S3_BUCKET}/${ZIP_FILE_KEY}
}

deploy () {
    echo "Updating code for function ${1}"
    aws lambda update-function-code \
        --function-name ${1} \
        --s3-bucket ${S3_BUCKET} \
        --s3-key ${ZIP_FILE_KEY} \
        --no-cli-pager
}

cleanup () {
    echo "Cleaning up..."
    rm ${original_wd}/function.zip
}

main () {
    source .env
    prep_deployment_package
    for lambda_function in ShopDiary
    do
        deploy $lambda_function
    done
    cleanup
}

main
