let currentImageIndex = 0;

function triggerNextImageUpload() {
    if (currentImageIndex >= 4) {
        alert("Você só pode adicionar até 4 imagens.");
        return;
    }
    document.getElementById(`id_images_${currentImageIndex}`).click();
}

function previewImage(event, index) {
    const file = event.target.files[0];
    if (!file) return;

    const previewContainer = document.getElementById('image-preview-container');

    const reader = new FileReader();
    reader.onload = function (e) {
        const imageDiv = document.createElement('div');
        imageDiv.style.position = 'relative';

        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.width = '100px';
        img.style.height = '100px';
        img.style.objectFit = 'cover';
        img.style.border = '1px solid #ccc';
        img.style.borderRadius = '8px';

        const removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.textContent = '✖';
        removeBtn.style.position = 'absolute';
        removeBtn.style.top = '0';
        removeBtn.style.right = '0';
        removeBtn.style.background = 'red';
        removeBtn.style.color = 'white';
        removeBtn.style.border = 'none';
        removeBtn.style.borderRadius = '50%';
        removeBtn.style.cursor = 'pointer';

        removeBtn.onclick = () => {
            imageDiv.remove();
            document.getElementById(`id_images_${index}`).value = "";
            currentImageIndex--;
        };

        imageDiv.appendChild(img);
        imageDiv.appendChild(removeBtn);
        previewContainer.appendChild(imageDiv);

        currentImageIndex++;
    };
    reader.readAsDataURL(file);
}