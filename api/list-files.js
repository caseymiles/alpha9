import { promises as fs } from 'fs';
import path from 'path';

export default async function handler(req, res) {
    const { folder } = req.query;

    try {
        const directory = path.join(process.cwd(), folder);

        const files = await fs.readdir(directory);

        const visibleFiles = files.filter(file => !file.startsWith('.'));

        res.status(200).json(visibleFiles);
    } catch (error) {
        console.error('Error reading directory:', error);
        res.status(500).json({ error: 'Failed to list files' });
    }
}

