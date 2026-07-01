# ICAMP · Nueva web (propuesta)

Nueva página de inicio para **icamp.es** — Instituto Canario de Marcas y Patentes.
Rediseño con foco en **SEO extremo (Google + IA), usabilidad y accesibilidad (WCAG 2.1 AA)**.

## Contenido de la entrega

| Archivo | Descripción |
|---|---|
| `index.html` | Página de inicio. |
| `marcas.html` | Página de servicio: registro de marcas y nombres comerciales. |
| `patentes.html` | Página de servicio: patentes y modelos de utilidad. |
| `diseno-industrial.html` | Página de servicio: diseño industrial. |
| `blog.html` | Índice del blog. |
| `cuanto-cuesta-registrar-una-marca.html` | Artículo destacado (guía de precios). |
| `styles.css` | Hoja de estilos compartida (sistema de diseño, cacheada en todas las páginas). |
| `app.js` | JavaScript compartido (menú, formulario, año). |
| `og-image.jpg` · `logo.png` · `favicon.svg` | Imagen social, logotipo y favicon. |
| `robots.txt` | Rastreo abierto + permiso explícito a bots de IA (GEO). |
| `sitemap.xml` | Mapa del sitio (6 URLs). |
| `site.webmanifest` | Manifiesto PWA básico. |
| `ESTRATEGIA-SEO.md` | Estrategia de palabras clave, SEO técnico, GEO y accesibilidad. |
| `generate_assets.py` | Script para regenerar `og-image.jpg` / `logo.png`. |

## Cómo verla

Abre `index.html` en cualquier navegador. Para navegar entre páginas con enlaces
limpios (`/marcas/`, `/patentes/`…) hace falta un servidor web.

## Despliegue

Sube todos los archivos a la raíz de `www.icamp.es`. Los enlaces internos usan URLs
limpias con barra final (`/marcas/`, `/patentes/`, `/diseno-industrial/`, `/blog/`,
`/blog/cuanto-cuesta-registrar-una-marca/`) que **coinciden con la estructura de
permalinks actual del sitio**, por lo que no hacen falta redirecciones. Cada `.html`
debe servirse en su ruta con barra final (en WordPress, como página/entrada con ese slug;
en un hosting estático, mediante reglas de reescritura).

## Características técnicas

- **SEO on-page**: `<title>`/description optimizados, keywords locales, jerarquía H1–H3, enlazado interno.
- **Datos estructurados**: JSON-LD `@graph` (LegalService, WebSite, BreadcrumbList, FAQPage) con NAP, geo, horario y catálogo de precios.
- **Social**: Open Graph + Twitter Cards.
- **GEO/AEO**: FAQ con respuestas directas + `robots.txt` que autoriza bots de IA.
- **Accesibilidad WCAG 2.1 AA**: skip link, landmarks, foco visible, contraste AA, teclado, formulario accesible, `prefers-reduced-motion`.
- **Rendimiento**: cero dependencias externas, CSS crítico en línea, SVG en línea, fuentes del sistema.
- **Responsive**: móvil, tablet y escritorio.

## ⚠️ Antes de publicar

Ver sección "Datos a confirmar por el cliente" en `ESTRATEGIA-SEO.md`
(cifras de experiencia/clientes, plazos, coordenadas GPS, reseñas) y conectar el
formulario de contacto a un backend/email real.

---

*Made in Italy* 🇮🇹
