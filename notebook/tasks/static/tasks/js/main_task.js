document.addEventListener('DOMContentLoaded', function() {
  const editButtons = document.querySelectorAll('.edit-button');
  const showCreateFormButton = document.getElementById('show-create-form');
  const createForm = document.getElementById('create-form');

  showCreateFormButton.addEventListener('click', function() {
    if (createForm.style.display === 'none' || createForm.style.display === '') {
      createForm.style.display = 'block';
    } else {
      createForm.style.display = 'none';
    }
  });

  editButtons.forEach(button => {
    button.addEventListener('click', function() {
      const id = button.getAttribute('data-id');
      const form = document.querySelector(`.edit-form[data-id="${id}"]`);
      const nameField = form.querySelector('input[title="title"]');
      const descriptionField = form.querySelector('textarea[name="description"]');
      const nameText = form.parentElement.querySelector('.title');
      const descriptionText = form.parentElement.querySelector('.description');


      if (form.style.display === 'none') {
        form.style.display = 'block';
        nameField.value = nameText.textContent;
        descriptionField.value = descriptionText.textContent;
        nameText.style.display = 'none';
        descriptionText.style.display = 'none';
      } else {
        form.style.display = 'none';
        nameText.textContent = nameField.value;
        descriptionText.textContent = descriptionField.value;
        nameText.style.display = 'inline';
        descriptionText.style.display = 'inline';
      }
    });
  });
});
