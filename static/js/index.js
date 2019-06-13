$(document).ready(() => {
    $('#predict-btn').click(() => {
        let text = $('#predict-text').val();
    
        $.post('/predict', {
            'text' : text
        })
        .done(data => {
            $('#predict-result-panel').removeClass('w3-green w3-deep-orange w3-gray w3-red');
            
            if (data.status == 'failed') {
                $('#predict-result-panel').addClass('w3-red');
                $('#predict-result-text').text('Ошибка классификации');
            }
            else if (data.status == 'neutral or not sure') {
                $('#predict-result-panel').addClass('w3-gray');
                $('#predict-result-text').text('Класс нейтральный или классификатор не уверен');
            }
            else {
                if (data.class == 'pos') {
                    var predicted_class = 'положительный';
                }
                else if (data.class == 'neg') {
                    var predicted_class = 'негативный';
                }

                if (data.status == 'possibly') {
                    $('#predict-result-text').text(`Возможно ${predicted_class}`);
                }
                else if (data.status == 'exactly') {
                    $('#predict-result-text').text(`Точно ${predicted_class}`);
                }

                if (data.class == 'neg') {
                    $('#predict-result-panel').addClass('w3-deep-orange');
                }
                else if (data.class == 'pos') {
                    $('#predict-result-panel').addClass('w3-green');
                }
            }
        })
    });

    $('#clear-predict-text-btn').click(() => {
        $('#predict-text').val('');
        $('#predict-result-text').text('');

        $('#predict-result-panel').removeClass('w3-green w3-deep-orange w3-gray w3-red');
    });
});