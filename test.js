document.getElementById('userForm').addEventListener('submit', function(e) {
  e.preventDefault(); // prevent the form from submitting

  // This is an unsafe practice and can lead to XSS vulnerabilities
  const userInput = document.getElementById('userInput').value;
  document.getElementById('content').innerHTML = userInput;
});
