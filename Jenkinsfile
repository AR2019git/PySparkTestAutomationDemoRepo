// Filename: Jenkinsfile
node {
  def GITREPOREMOTE = "https://github.com/AR2019git/PySparkTestAutomationDemoRepo.git"
  def GITBRANCH     = "master"
  def DBCLIPATH     = "/usr/local/bin"
  def JQPATH        = "/usr/local/bin"
  def JOBPREFIX     = "PySparkTestAutomationCICDJob"
  def BUNDLETARGET  = "dev"
  def DATABRICKSDCONFIGUREFILE = "dbrickscliconfig"

  stage('Checkout') {
    sh "echo Hello Ajit"
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('Check Databricks') {

    sh """#!/bin/bash
          echo $DATABRICKS_CLIENT_SECRET
          echo $DATABRICKS_CLIENT_ID
          echo $DATABRICKS_HOST
       """
  }
  stage('Validate Bundle') {
    sh """#!/bin/bash
          echo ${DATABRICKS_CLIENT_ID}
          ${DBCLIPATH}/databricks bundle validate -t ${BUNDLETARGET}
       """
  }
 stage('Deploy Bundle') {
    sh """#!/bin/bash
          echo "Skipping  Deploy Bundle"
         # ${DBCLIPATH}/databricks bundle deploy -t ${BUNDLETARGET}
       """
  }
  stage('Run Unit Tests') {
    sh """#!/bin/bash
           echo "Skipping  Unit Test Runs"
         # ${DBCLIPATH}/databricks bundle run -t ${BUNDLETARGET} run-unit-tests
       """
  }
  stage('Run Notebook') {
    sh """#!/bin/bash
        echo "Skipping Evaluate DABDEMO Runs"

          #${DBCLIPATH}/databricks bundle run -t ${BUNDLETARGET} run-dabdemo-notebook
       """
  }
  stage('Evaluate Notebook Runs') {
    sh """#!/bin/bash
       echo "Skipping Evaluate Notebook Runs"
        #${DBCLIPATH}/databricks bundle run -t ${BUNDLETARGET} evaluate-notebook-runs
       """
  }
  
  stage('Import Test Results') {
    def DATABRICKS_BUNDLE_WORKSPACE_ROOT_PATH
    def getPath = "${DBCLIPATH}/databricks bundle validate -t ${BUNDLETARGET} | ${JQPATH}/jq -r .workspace.file_path"
    def output = sh(script: getPath, returnStdout: true).trim()

   sh """#!/bin/bash
      echo "SKipping Testr Results Import as it does not get source direcory on Workspace"
       echo "output"
       echo ${output}

       """
    
    if (output) {
      DATABRICKS_BUNDLE_WORKSPACE_ROOT_PATH = "${output}"
    } else {
      error "Failed to capture output or command execution failed: ${getPath}"
    }

    sh """#!/bin/bash
         # ${DBCLIPATH}/databricks workspace export-dir \
         # ${DATABRICKS_BUNDLE_WORKSPACE_ROOT_PATH}/Validation/Output/test-results \
         # ${WORKSPACE}/Validation/Output/test-results \
         # -t ${BUNDLETARGET} \
         # --overwrite
       """
  }
  stage('Publish Test Results') {
    junit allowEmptyResults: true, testResults: '/Users/ajitrajan/documents/GitHub/PySparkTestAutomationDemoRepo/testresults/*.xml', skipPublishingChecks: true
  
}

  }
}
