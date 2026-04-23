#!/bin/bash


load_credentials() {
    eval "$(python3 $SCRIPTS_DIR/load-credentials.py )"
}

initialise_environment() {
    TF_DIR="$ROOT_DIR/aws/environments/development"
    TF_VARIABLES_FILE="$ROOT_DIR/aws/environments/development/terraform.tfvars"
    load_credentials
}


run_localstack() {
    docker compose -f docker-compose.dev.yml up -d
}

run_terraform_init() {
    terraform -chdir=$TF_DIR init
}

run_terraform_plan() {
    terraform -chdir=$TF_DIR plan -var-file=$TF_VARIABLES_FILE
}

run_terraform_apply() {
    terraform -chdir=$TF_DIR apply -var-file=$TF_VARIABLES_FILE
}

run_terraform_destroy() {
    terraform -chdir=$TF_DIR destroy -var-file=$TF_VARIABLES_FILE
}


main() {

    initialise_environment # Load credentials and set up environment variables
    run_localstack # Start LocalStack

    while true; do
        read -p "What action would you like to perform? (init, plan, apply, destroy, exit): " ACTION
        case $ACTION in
            init)
                run_terraform_init
                ;;
            plan)
                run_terraform_plan
                ;;
            apply)
                run_terraform_apply
                ;;
            destroy)
                run_terraform_destroy
                ;;
            exit)
                break
                ;;
            *)
                echo "Invalid action. Please try again."
                ;;
        esac
    done
}

main