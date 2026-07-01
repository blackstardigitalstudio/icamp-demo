# Estrategia SEO · ICAMP — Instituto Canario de Marcas y Patentes

> Documento de estrategia para la nueva página de **icamp.es**.
> Objetivo: posicionamiento SEO extremo (Google + motores de IA) con máxima usabilidad y accesibilidad.

---

## 1. Diagnóstico del negocio

**ICAMP** es una Oficina Internacional de Marcas y Patentes (Agentes de la Propiedad Industrial) con sede en **Las Palmas de Gran Canaria** y clientela también en **Santa Cruz de Tenerife**. Servicios: registro y defensa de **marcas y nombres comerciales, patentes y modelos de utilidad, diseño industrial y marca UE/internacional**.

**Activos diferenciales detectados** (a explotar en SEO y conversión):
- **Transparencia de tarifas**: publican precios reales → confianza + captación de búsquedas "precio / cuánto cuesta".
- **Cartera de clientes reconocibles** (Macaronesian Gin, KN Hoteles, Mojo Surf, Arenas del Mar) → prueba social local.
- **Doble presencia canaria** → doble oportunidad de SEO local.
- **Equipo multidisciplinar** (agentes europeos, ingenieros, químicos) → autoridad E-E-A-T.

---

## 2. Estrategia de palabras clave

La competencia por keywords nacionales genéricas ("registrar marca") es altísima y dominada por grandes agregadores. **La ventaja competitiva de ICAMP es geográfica y de confianza.** Por eso priorizamos:

### 🥇 Prioridad 1 — Local + comercial (máxima conversión, baja competencia)
- registro de marcas Las Palmas / Gran Canaria
- registro de marcas Tenerife / Canarias
- agente de la propiedad industrial Canarias / Las Palmas
- registrar patente Canarias
- abogado de marcas Gran Canaria

### 🥈 Prioridad 2 — Servicios (comercial)
- registrar una marca · registro de nombre comercial
- registrar una patente · modelo de utilidad
- registro de diseño industrial
- marca de la Unión Europea (EUIPO) · marca internacional (OMPI)

### 🥉 Prioridad 3 — Informativo (TOFU + captación en IA / AI Overviews)
- cuánto cuesta registrar una marca en España
- cómo registrar una marca · pasos
- qué es una marca / un diseño industrial
- diferencia entre marca nacional y marca de la UE

### Mapa de intención → sección de la página
| Cluster | Dónde se ataca en la página |
|---|---|
| Local comercial | `<title>`, H1, hero, sección Contacto (NAP), schema LocalBusiness |
| Servicios | Sección "Servicios" (H2/H3 + tarjetas), tabla de Tarifas |
| Informativo/GEO | Sección FAQ (con `FAQPage` schema), "Cómo trabajamos" |

---

## 3. SEO técnico implementado

- **`<title>` y meta description** optimizados con keyword local + marca.
- **Datos estructurados JSON-LD** (`@graph`): `LegalService`/`ProfessionalService`, `WebSite`, `BreadcrumbList` y `FAQPage`, con dirección, geolocalización, horario, `areaServed`, `sameAs` y catálogo de servicios con precios.
- **Open Graph + Twitter Cards** para compartición en redes.
- **`hreflang`** (es-ES + x-default) y **canonical**.
- **`robots.txt`** con permiso explícito a bots de IA (GPTBot, PerplexityBot, ClaudeBot, Google-Extended…) para **GEO/AEO**.
- **`sitemap.xml`** y **`site.webmanifest`** (PWA básica) + favicon SVG.
- **Jerarquía semántica**: un único `<h1>`, `<h2>` por sección, landmarks ARIA.
- **Rendimiento**: CSS crítico en línea, **cero dependencias externas**, SVG en línea, fuentes del sistema → carga casi instantánea y máxima privacidad.

---

## 4. Optimización para motores de IA (GEO / AEO)

- **Respuestas directas** en la FAQ (formato pregunta → respuesta concisa) marcadas con `FAQPage`.
- **Entidades claras** (OEPM, EUIPO, OMPI, propiedad industrial) para desambiguación.
- **Datos concretos** (precios, plazos) que los LLM pueden citar.
- **robots.txt** que autoriza el rastreo por IA.

---

## 5. Accesibilidad (WCAG 2.1 AA)

Skip link, landmarks semánticos, foco visible, contraste AA, navegación por teclado, acordeón accesible (`<details>`), formulario con `label`/`aria-required`/`aria-live`, objetivos táctiles ≥44 px, `prefers-reduced-motion`, textos alternativos e iconos decorativos ocultos a lectores de pantalla.

---

## 6. Datos a confirmar por el cliente ⚠️

Algunas cifras son estimaciones de marketing y **deben validarse** antes de publicar:
- **"+25 años"** de experiencia.
- **"+300 empresas"** / número de clientes.
- **"6–8 meses"** de plazo de registro (verificar con plazos OEPM actuales).
- **Coordenadas GPS** exactas de la oficina (ajustar en el schema).
- **Reseñas / valoraciones**: si hay reseñas de Google, añadir `aggregateRating` al schema (mejora los rich results).

---

## 7. Próximos pasos recomendados (fase 2)

1. **Google Business Profile** optimizado en Las Palmas y Tenerife (clave para el SEO local).
2. **Páginas de servicio individuales** (marcas / patentes / diseño) para profundidad temática.
3. **Blog** con contenidos informativos ("cómo registrar…", casos) para autoridad y long-tail.
4. **Reseñas** y su marcado `aggregateRating`.
5. **Backlinks locales** (cámaras de comercio, directorios canarios, prensa económica).
6. Conectar el **formulario** a un backend/email real y medir con analítica.

---

*Made in Italy* 🇮🇹 — Estrategia y desarrollo preparados con metodología multi-agente.
