const childProcess = require('child_process');

function cloneRepo(userInput) {
    childProcess.spawn('git', ['clone', userInput]);
}
