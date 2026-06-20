import {
  expectBaseLayout,
  expectMainNavigation,
} from '../support/common/common.assertions';

const pages = [
  {
    name: 'Home',
    path: '/',
  },
  {
    name: 'Practice',
    path: '/practice/',
  },
];

describe('Base layout', () => {
  pages.forEach(({ name, path }) => {
    it(`should show base layout on ${name} page`, () => {
      cy.visit(path);

      cy.location('pathname').should('eq', path);

      expectBaseLayout();
      expectMainNavigation();
    });
  });
});
