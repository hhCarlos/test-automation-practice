import {
  expectBaseLayout,
  expectMainNavigation,
} from '../../support/common/common.assertions';

const PAGE_PATH = '/';

describe('Home page', () => {
  it('should open the home page and show the base layout', () => {
    cy.visit(PAGE_PATH);

    cy.location('pathname').should('eq', PAGE_PATH);

    expectBaseLayout();
    expectMainNavigation();
  });
});
