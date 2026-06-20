import { commonSelectors } from './common.selectors';

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