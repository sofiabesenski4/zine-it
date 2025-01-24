import { defineConfig } from 'cypress';

export default defineConfig({
  defaultCommandTimeout: 1000,
  e2e: {
    baseUrl: 'http://localhost:3001'
  }
});
