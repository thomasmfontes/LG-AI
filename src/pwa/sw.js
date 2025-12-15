self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(clients.claim());
});

self.addEventListener('fetch', (event) => {
    // Estratégia simples: Apenas responde, permitindo cache do navegador padrão
    // Para Gradio, evitar cache agressivo em APIs é importante
    event.respondWith(fetch(event.request));
});
