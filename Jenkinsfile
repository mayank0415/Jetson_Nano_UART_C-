node {     
    
    stage('Initialize') {
        checkout scm // "scm" equates to the configuration that the job was run with
        if (env.TAG_NAME == null) {
           PKG_VERSION="1.0.0"
        } else {
           PKG_VERSION=env.TAG_NAME
        }
    }
    
    stage('Build') {
        echo 'Within Stage Build'
        echo "BRANCH_NAME is ${env.BRANCH_NAME}"
        echo "BRANCH_IS_PRIMARY is ${env.BRANCH_IS_PRIMARY}"
        echo "CHANGE_BRANCH is ${env.CHANGE_BRANCH}"
        echo "TAG_NAME is ${env.TAG_NAME}"
        echo "TAG_TIMESTAMP is ${env.TAG_TIMESTAMP}"
        echo "Printing: Package Version taken, is ${PKG_VERSION}"
        sh """
        #!/bin/bash
        whoami
        ls -alh
        pwd
        ~/.conan2/conan-easy-jenkins-with-version.py build --version $PKG_VERSION
        """
    }
    
    stage('Remove') {
        echo 'Within Stage Remove'
        if (env.TAG_NAME == null) {
           sh """
           ~/.conan2/conan-remove.py --version $PKG_VERSION
           """
        }
    }

    stage('Check_Status') {
        echo 'Within Stage Check_Status'
        try {
           sh '~/.conan2/conan-check-create-exit-status.py'
        } catch (Exception ex) {
           println("Exception or error description: " + ex.toString())
           sh """
           ~/.conan2/conan-remove.py --version $PKG_VERSION
           """
           error("Intentionally creating error after handling exception since at least one conan create command exit status was non-zero (failure)")
        } 
    }

    stage('Upload') {
        echo 'Within Stage Upload'
        if (env.TAG_NAME != null) {
           sh """
           ~/.conan2/conan-upload.py --version $PKG_VERSION
           """
        }
    }

    stage('Remove_All') {
        echo 'Within Stage Remove_All'
    }

}

