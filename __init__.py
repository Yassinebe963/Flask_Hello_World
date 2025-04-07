<!DOCTYPE html>
<html>
<body>
  <pre id="pyramide"></pre>
  <script>
    let n = 5;
    let output = "";
    for (let i = 1; i <= n; i++) {
      output += " ".repeat(n - i) 
               + Array.from({length: i}, (_, j) => j + 1).join('') 
               + Array.from({length: i - 1}, (_, j) => i - 1 - j).join('') 
               + "\n";
    }
    document.getElementById("pyramide").textContent = output;
  </script>
</body>
</html>
