  console.log('Js file loaded');
  
  function openModal(src) {
    document.getElementById('modal-image').src = src;
    document.getElementById('myModal').style.display = 'block';
    document.getElementById('myModal').style.transition = 'color 1s ease';
    //   transition: color 0.3s ease;
  }

  function closeModal() {
    document.getElementById('myModal').style.display = 'none';
  }