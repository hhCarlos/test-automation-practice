import {
  expectBaseLayout,
  expectMainNavigation,
} from '../../support/common/common.assertions';

const PAGE_PATH = '/courses/';

describe('Courses page', () => {
  it('should open the courses page and show the base layout', () => {
    cy.visit(PAGE_PATH);

    cy.location('pathname').should('eq', PAGE_PATH);

    expectBaseLayout();
    expectMainNavigation();
  });
});
