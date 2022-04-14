properties([parameters([string(defaultValue: 'aviel', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/avielb/DevOps2402.git"
    }
    stage("bla") {
        bat "dir"
    }
}
