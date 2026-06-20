# Automation Practice

Este repositorio contiene una demo de automatización de pruebas usando diferentes herramientas.

Actualmente el proyecto tiene una primera implementación con **Cypress** y una carpeta preparada para una futura implementación con **Selenium + Python**.

El objetivo principal es practicar fundamentos de automatización de pruebas de forma ordenada:

* cómo estructurar pruebas E2E
* cómo separar pruebas por módulo
* cómo reutilizar selectores
* cómo reutilizar assertions comunes
* cómo correr pruebas en modo visual y headless
* cómo preparar una base que pueda crecer con más casos de prueba

---

## Sitio bajo prueba

Las pruebas usan como sitio de práctica:

```txt
https://practicetestautomation.com/
```

Este sitio contiene páginas diseñadas para practicar automatización, por ejemplo:

* Home
* Practice
* Login test
* Exceptions test
* Tables test

---

## Estructura del repositorio

```txt
automation-practice/
  README.md
  .gitignore

  cypress-automation/
    package.json
    package-lock.json
    cypress.config.js
    README.md

    cypress/
      e2e/
        home.cy.js
        practice.cy.js
        layout.cy.js
        courses.cy.js
        blog.cy.js
        contact.cy.js

      fixtures/

      support/
        assertions/
          common.assertions.js

        selectors/
          common.selectors.js
          practice.selectors.js

        commands.js
        e2e.js

  selenium-automation/
    README.md
```

---

## Requisitos previos

Antes de correr el proyecto necesitas tener instalado lo siguiente:

### 1. Git

Git se usa para clonar el repositorio y trabajar con control de versiones.

Para validar si ya lo tienes instalado:

```bash
git --version
```

Si el comando responde con una versión, Git ya está instalado.

---

### 2. Node.js

Cypress corre sobre Node.js, por eso necesitas tener instalado Node.

Para validar si ya lo tienes instalado:

```bash
node --version
```

También valida npm:

```bash
npm --version
```

Se recomienda usar una versión moderna de Node, por ejemplo Node 20 o superior.

---

### 3. Navegador

Cypress puede correr con navegadores como:

* Chrome
* Electron
* Edge
* Firefox

Para desarrollo local normalmente se recomienda usar Chrome o Electron.

---

## Cómo clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd automation-practice
```

Ejemplo:

```bash
git clone https://github.com/<usuario>/automation-practice.git
cd automation-practice
```

---

## Cómo instalar dependencias de Cypress

Desde la raíz del proyecto, entra a la carpeta de Cypress:

```bash
cd cypress-automation
```

Instala las dependencias:

```bash
npm install
```

Este comando instalará Cypress y las dependencias necesarias dentro de la carpeta:

```txt
cypress-automation/node_modules/
```

---

## Configuración de Cypress

El archivo principal de configuración está en:

```txt
cypress-automation/cypress.config.js
```

La configuración base debería verse así:

```js
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  allowCypressEnv: false,

  e2e: {
    baseUrl: 'https://practicetestautomation.com',
  },
});
```

Gracias a `baseUrl`, las pruebas pueden visitar rutas relativas.

Ejemplo:

```js
cy.visit('/');
cy.visit('/practice/');
cy.visit('/practice-test-login/');
```

En lugar de escribir la URL completa cada vez:

```js
cy.visit('https://practicetestautomation.com/practice/');
```

---

## Scripts disponibles

Dentro de `cypress-automation/package.json` deberían existir estos scripts:

```json
{
  "scripts": {
    "cy:open": "cypress open",
    "cy:run": "cypress run --browser chrome --headless"
  }
}
```

---

## Cómo abrir Cypress en modo visual

Este modo sirve para desarrollar, depurar y ver las pruebas corriendo en el navegador.

Desde la carpeta `cypress-automation`:

```bash
npm run cy:open
```

Esto abrirá la interfaz de Cypress.

Después:

1. Selecciona `E2E Testing`
2. Elige un navegador
3. Selecciona el archivo de prueba que quieres correr

Ejemplo:

```txt
home.cy.js
practice.cy.js
layout.cy.js
```

---

## Cómo correr Cypress en modo headless

Este modo corre las pruebas desde terminal, sin abrir la interfaz visual de Cypress.

Desde la carpeta `cypress-automation`:

```bash
npm run cy:run
```

Este comando es el que normalmente se usa en CI/CD.

---

## Cómo correr una sola prueba

Para correr un archivo específico:

```bash
npx cypress run --spec "cypress/e2e/practice.cy.js"
```

Otro ejemplo:

```bash
npx cypress run --spec "cypress/e2e/home.cy.js"
```

---

## Organización de pruebas

Los archivos `.cy.js` son archivos de prueba.

Ejemplo:

```txt
cypress/e2e/home.cy.js
cypress/e2e/practice.cy.js
cypress/e2e/layout.cy.js
```

Regla importante:

```txt
*.cy.js  -> archivos de prueba
*.js     -> selectores, datos, acciones, assertions o helpers
```

No se recomienda crear archivos como:

```txt
constants.cy.js
selectors.cy.js
helpers.cy.js
```

Porque Cypress puede interpretarlos como pruebas.

---

## Selectores

Los selectores viven en:

```txt
cypress/support/selectors/
```

Ejemplo:

```txt
common.selectors.js
practice.selectors.js
```

### Selectores comunes

Los selectores comunes son elementos que aparecen en varias páginas.

Ejemplo:

```js
export const commonSelectors = {
  layout: {
    header: '#site-header',
    main: '#main-container',
    footer: '#site-footer',
  },

  nav: {
    container: '#menu-primary',
    list: '#menu-primary-items',
    items: '#menu-primary-items > li',
    links: '#menu-primary-items a',

    homeItem: '#menu-item-43',
    practiceItem: '#menu-item-20',
    coursesItem: '#menu-item-21',
    blogItem: '#menu-item-19',
    contactItem: '#menu-item-18',

    homeLink: '#menu-item-43 > a',
    practiceLink: '#menu-item-20 > a',
    coursesLink: '#menu-item-21 > a',
    blogLink: '#menu-item-19 > a',
    contactLink: '#menu-item-18 > a',
  },
};
```

### Selectores por módulo

Cada página o módulo puede tener su propio archivo de selectores.

Ejemplo:

```txt
practice.selectors.js
```

```js
export const practiceSelectors = {
  content: {
    postContent: '#main-container .post-content',
  },

  links: {
    testLoginPage: 'a[href*="/practice-test-login/"]',
    testExceptionsPage: 'a[href*="/practice-test-exceptions/"]',
    testTablePage: 'a[href*="/practice-test-table/"]',
  },
};

export const practiceLinks = {
  testLoginPage: {
    path: '/practice-test-login/',
    text: 'Test Login Page',
  },
  testExceptionsPage: {
    path: '/practice-test-exceptions/',
    text: 'Test Exceptions',
  },
  testTablePage: {
    path: '/practice-test-table/',
    text: 'Test Table',
  },
};
```

---

## Assertions comunes

Las assertions comunes viven en:

```txt
cypress/support/assertions/
```

Ejemplo:

```txt
common.assertions.js
```

Este archivo contiene validaciones reutilizables para no repetir código en cada prueba.

```js
import { commonSelectors } from '../selectors/common.selectors';

export const expectBaseLayout = () => {
  cy.get(commonSelectors.layout.header)
    .should('be.visible');

  cy.get(commonSelectors.layout.main)
    .should('be.visible');

  cy.get(commonSelectors.layout.footer)
    .should('exist');
};

export const expectMainNavigation = () => {
  cy.get(commonSelectors.nav.container)
    .should('be.visible');

  cy.get(commonSelectors.nav.list)
    .should('be.visible');

  cy.get(commonSelectors.nav.links)
    .should('have.length.at.least', 1);
};
```

Nota importante:

El footer se valida con `exist` y no con `be.visible` porque en algunas páginas existe en el DOM, pero puede tener altura `0px`. En ese caso Cypress no lo considera visible.

---

## Ejemplo de prueba básica

```js
import {
  expectBaseLayout,
  expectMainNavigation,
} from '../support/assertions/common.assertions';

const PAGE_PATH = '/';

describe('Home page', () => {
  it('should open the home page and show the base layout', () => {
    cy.visit(PAGE_PATH);

    cy.location('pathname').should('eq', PAGE_PATH);

    expectBaseLayout();
    expectMainNavigation();
  });
});
```

Esta prueba valida:

1. que se pueda abrir la página Home
2. que la URL sea correcta
3. que exista el layout base
4. que exista la navegación principal

---

## Ejemplo de prueba para Practice

```js
import {
  expectBaseLayout,
  expectMainNavigation,
} from '../support/assertions/common.assertions';

import {
  practiceSelectors,
  practiceLinks,
} from '../support/selectors/practice.selectors';

const PAGE_PATH = '/practice/';

describe('Practice page', () => {
  it('should show practice exercise links', () => {
    cy.visit(PAGE_PATH);

    cy.get(practiceSelectors.content.postContent)
      .should('be.visible');

    const links = [
      {
        selector: practiceSelectors.links.testLoginPage,
        ...practiceLinks.testLoginPage,
      },
      {
        selector: practiceSelectors.links.testExceptionsPage,
        ...practiceLinks.testExceptionsPage,
      },
      {
        selector: practiceSelectors.links.testTablePage,
        ...practiceLinks.testTablePage,
      },
    ];

    links.forEach(({ selector, text, path }) => {
      cy.get(selector)
        .should('be.visible')
        .and('contain.text', text)
        .and('have.attr', 'href')
        .and('include', path);
    });
  });
});
```

Esta prueba valida que la página Practice tenga los links esperados hacia los ejercicios.

---

## Buenas prácticas usadas en este proyecto

### 1. No repetir selectores en todas las pruebas

Mal ejemplo:

```js
cy.get('#menu-primary-items a');
```

Mejor:

```js
cy.get(commonSelectors.nav.links);
```

---

### 2. Usar rutas relativas

Mal ejemplo:

```js
cy.visit('https://practicetestautomation.com/practice/');
```

Mejor:

```js
cy.visit('/practice/');
```

---

### 3. Separar pruebas por responsabilidad

La página Practice solo debe probar cosas de Practice.

Ejemplo:

```txt
Practice prueba:
- que carga /practice/
- que muestra layout base
- que muestra links de ejercicios
- que navega hacia Test Login Page
```

Login debe probar login.

Ejemplo:

```txt
Login prueba:
- login exitoso
- usuario inválido
- password inválido
- logout
```

---

### 4. Cada prueba debe poder correr sola

No se debe depender de que una prueba anterior haya dejado el sistema en cierto estado.

Mal ejemplo:

```txt
Test 1 hace login
Test 2 asume que ya hay sesión iniciada
```

Mejor:

```txt
Cada test prepara lo que necesita
Cada test valida su propio resultado
```

---

### 5. No usar selectores demasiado genéricos

Mal ejemplo:

```js
cy.get('a');
cy.get('button');
cy.get('div');
```

Mejor:

```js
cy.get('a[href*="/practice-test-login/"]');
cy.get('#submit');
cy.get('#main-container .post-content');
```

---

## Flujo recomendado para trabajar

Antes de empezar un cambio:

```bash
git pull
```

Crear una rama:

```bash
git checkout -b feature/add-login-tests
```

Entrar a Cypress:

```bash
cd cypress-automation
```

Correr Cypress visual:

```bash
npm run cy:open
```

Cuando las pruebas estén listas, correr headless:

```bash
npm run cy:run
```

Regresar a la raíz:

```bash
cd ..
```

Agregar cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "test: add login tests"
```

Subir rama:

```bash
git push origin feature/add-login-tests
```

---

## Checklist antes de subir cambios

Antes de hacer push, valida:

* [ ] Las pruebas corren localmente
* [ ] No agregaste `node_modules`
* [ ] No dejaste archivos temporales
* [ ] No duplicaste selectores innecesariamente
* [ ] Los nombres de los tests explican qué validan
* [ ] Cada test puede correr de forma independiente
* [ ] Si agregaste una página nueva, agregaste sus selectores en `support/selectors`

---

## Problemas comunes

### Cypress no abre

Prueba reinstalar dependencias:

```bash
rm -rf node_modules package-lock.json
npm install
```

Luego:

```bash
npm run cy:open
```

---

### `cy.visit('/')` no abre el sitio correcto

Revisa que `cypress.config.js` tenga configurado `baseUrl`:

```js
e2e: {
  baseUrl: 'https://practicetestautomation.com',
}
```

---

### Una prueba falla porque un elemento no es visible

Revisa si realmente necesitas validar visibilidad.

Ejemplo:

```js
cy.get(selector).should('be.visible');
```

Si solo necesitas validar que el elemento existe en el DOM:

```js
cy.get(selector).should('exist');
```

---

### Cypress no encuentra un selector

Revisa:

1. que el selector exista en el DOM
2. que no esté dentro de otro iframe
3. que la página correcta haya cargado
4. que el selector esté bien escrito
5. que el elemento no aparezca después de una acción o espera

---

## Estado actual del proyecto

Actualmente está implementada la base de Cypress con:

* configuración inicial
* pruebas E2E
* selectores comunes
* assertions comunes
* pruebas de páginas principales
* validación de links en Practice

La carpeta de Selenium está preparada para una siguiente etapa.

---

## Siguientes pasos sugeridos

* Agregar pruebas completas para Login
* Agregar pruebas para Logout
* Agregar pruebas para Exceptions
* Agregar pruebas para Tables
* Agregar Selenium + Python
* Agregar ejecución en CI/CD con GitHub Actions
* Agregar reportes de ejecución
* Documentar casos de prueba por módulo
