// Function to dynamically load files
function loadFiles(folder, containerId, type = 'image') {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear container

    fetch(`/api/files?folder=${folder}`)
        .then((response) => response.json())
        .then((files) => {
            files.forEach((file) => {
                const link = document.createElement('a');
                link.href = `/${folder}/${file}`;
                link.target = '_blank';

                if (type === 'image') {
                    const thumbnail = document.createElement('img');
                    thumbnail.src = `/${folder}/${file}`;
                    thumbnail.alt = file;
                    thumbnail.className = 'thumbnail';
                    link.appendChild(thumbnail);
                }

                container.appendChild(link);
            });
        })
        .catch((error) => {
            console.error(`Error loading files from ${folder}:`, error);
        });
}
