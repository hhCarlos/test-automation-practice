import {
  expectBaseLayout,
  expectMainNavigation,
} from '../../support/common/common.assertions';

import {
  practiceSelectors,
  practiceLinks,
} from '../../support/features/practice/practice.selectors';

const PAGE_PATH = '/practice/';

describe('Practice page', () => {
  it('should open the practice page and show the base layout', () => {
    cy.visit(PAGE_PATH);

    cy.location('pathname').should('eq', PAGE_PATH);

    expectBaseLayout();
    expectMainNavigation();
  });

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

  it('should navigate to test login page from practice page', () => {
    cy.visit(PAGE_PATH);

    cy.get(practiceSelectors.links.testLoginPage)
      .should('be.visible')
      .and('contain.text', practiceLinks.testLoginPage.text)
      .click();

    cy.location('pathname')
      .should('eq', practiceLinks.testLoginPage.path);
  });
});
