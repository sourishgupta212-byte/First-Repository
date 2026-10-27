    let folderHandle = null;

    document.getElementById('saveBtn').addEventListener('click', async () => {
        try {
            // 1. Ask for folder access ONCE. If already granted, it skips this popup.
            if (!folderHandle) {
                folderHandle = await window.showDirectoryPicker({ mode: 'readwrite' });
            }

            // 2. Automatically detect the name of the current file (e.g., "index.html")
            const currentFileName = window.location.pathname.split('/').pop() || 'index.html';

            // 3. Create or access that specific file inside your trusted folder
            const fileHandle = await folderHandle.getFileHandle(currentFileName, { create: true });

            // 4. Create a clean snapshot copy of your page
            const pageClone = document.documentElement.cloneNode(true);
            const liveEdits = document.getElementById('wikiContent').innerHTML;
            pageClone.querySelector('#wikiContent').innerHTML = liveEdits;

            // 5. Stream the changes straight to the file silently
            const fileStream = await fileHandle.createWritable();
            await fileStream.write('<!DOCTYPE html>\n' + pageClone.outerHTML);
            await fileStream.close();

            alert('Saved successfully without popups!');

        } catch (error) {
            console.error('Save system error:', error);
            alert('Could not save file. Ensure folder permissions are granted.');
        }
    });

