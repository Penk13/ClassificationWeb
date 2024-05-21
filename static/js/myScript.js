function predict() {
    const inputFile = document.getElementById('imageUpload').files[0];
    if (!inputFile) {
        alert('Please select an image file first.');
        return;
    }
    const formData = new FormData();
    formData.append('image', inputFile);

    const objectId = document.getElementById('predict-btn').getAttribute('data-object-id');
    formData.append('id', objectId);

    document.getElementById('predictionResult').innerText = '';
    document.getElementById('loading').style.display = 'block';

    $.ajax({
        url: '/predict/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#predictionResult').text(data.formatted_result);
            document.getElementById('loading').style.display = 'none';
        },
        error: function(error) {
            alert(error.responseJSON.error)
            document.getElementById('loading').style.display = 'none';
        }
    });
}