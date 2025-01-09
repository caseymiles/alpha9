// Load files dynamically for grids or lists
function loadLocalFiles(folder, containerId, type = 'image') {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear the container

    // Hardcoded list of files for demonstration purposes
    const files = {
        'src/art': ['art1.jpg', 'art2.jpg', 'art3.jpg'], // Add your actual art files here
        'src/videos': ['video1.mp4', 'video2.mp4'],
        'src/apps': ['app1.apk', 'app2.apk'],
        'src/podcasts': ['podcast1.mp3', 'podcast2.mp3'],
        'src/songs': ['song1.mp3', 'song2.mp3']
    };

    if (!files[folder]) return;

    files[folder].forEach((file) => {
        const link = document.createElement('a');
        link.href = `${folder}/${file}`;
        link.target = '_blank'; // Open in a new tab

        const thumbnail = document.createElement('img');
        thumbnail.src = `${folder}/${file}`;
        thumbnail.alt = file;
        thumbnail.className = 'thumbnail';

        link.appendChild(thumbnail);
        container.appendChild(link);
    });
}
