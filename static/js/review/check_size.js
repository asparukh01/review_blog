function checkFileSize() {
    let FS = document.getElementById("image");
    let files = FS.files;
  
    // Если выбран хотя бы один файл
    if (files.length > 0) {
      if (files[0].size > 1000 * 1024) {
        // Проверить ограничение
        FS.setCustomValidity("Размер файла не должен превышать 1 mB");
        return;
      }
    }
    // Если нарушения ограничений нет
    FS.setCustomValidity("");
  }


  window.onload = function () {
  document.getElementById("image").onchange = checkFileSize;
};