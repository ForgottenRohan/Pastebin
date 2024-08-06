
function selectText(textarea) {
    textarea.select(); // Выделяем текст
}

function copyText(textarea) {
    textarea.select(); // Выделяем текст
    try {
        // Копируем выделенный текст в буфер обмена
        const successful = document.execCommand('copy');
        const msg = successful ? 'Текст скопирован в буфер обмена!' : 'Не удалось скопировать текст.';
        alert(msg); // Обратная связь в консоли (можно вывести иное сообщение)
        
    } catch (err) {
        console.error('Ошибка при копировании текста: ', err);
    }
}
document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('.textarea');

    // Функция для автоматического изменения высоты
    function autoResize() {
        textarea.style.height = 'auto'; // Сбрасываем высоту
        textarea.style.height = (textarea.scrollHeight + 10) + 'px'; // Устанавливаем новую высоту
    }

    // Устанавливаем значение textarea и вызываем функцию изменения высоты
    textarea.value = textarea.value.trim(); // Убираем лишние пробелы
    autoResize(); // Вызываем функцию установки высоты при загрузке страницы
});
