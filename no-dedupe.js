const child_process = require('child_process');

function runUnsafeCommand(cmdType, userSuppliedValue) {
  // Concatenating command type and user-supplied value
  const fullCommand = `ls ${userSuppliedValue}`;
  
  // Using ternary operator to execute either exec or spawn
  cmdType === 'exec' ? child_process.exec(fullCommand) : child_process.spawn(fullCommand); // Unsafe
}

// Invoking the function
const userSuppliedValue = "user_input"; // This could be from an HTTP request, for instance

runUnsafeCommand('exec', userSuppliedValue);
runUnsafeCommand('spawn', userSuppliedValue);
