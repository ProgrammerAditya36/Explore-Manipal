// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();

  let alertWrappers = document.querySelectorAll('.alert');
  let alertCloses = document.querySelectorAll('.alert__close');

  console.log(alertWrappers); // Check if alertWrappers are selected
  console.log(alertCloses);   // Check if alertCloses are selected

  alertCloses.forEach(function (alertClose, index) {
    alertClose.addEventListener('click', function () {
      alertWrappers[index].style.display = 'none';
      console.log('Alert closed.'); // Check if the click event is triggered
    });
  });
});
