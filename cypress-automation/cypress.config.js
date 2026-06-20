const { defineConfig } = require('cypress');

module.exports = defineConfig({
  allowCypressEnv: false,

  e2e: {
    baseUrl: 'https://practicetestautomation.com',
    viewportWidth: 1440,
    viewportHeight: 900,
  },
});
