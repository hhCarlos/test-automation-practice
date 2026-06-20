import { loginData } from '../../support/features/login/login.data';
import { login, logout } from '../../support/features/login/login.actions';
import { loginSelectors } from '../../support/features/login/login.selectors';

describe('Login page', () => {
  it('should login successfully with valid credentials', () => {
    cy.visit(loginData.paths.login);

    login(loginData.validUser);

    cy.location('pathname')
      .should('eq', loginData.paths.success);

    cy.get(loginSelectors.success.title)
      .should('be.visible')
      .and('contain.text', loginData.success.title);

    cy.get(loginSelectors.success.content)
      .should('be.visible')
      .and('contain.text', loginData.success.expectedText);

    cy.get(loginSelectors.success.logoutButton)
      .should('be.visible')
      .and('contain.text', loginData.success.logoutText);
  });

  it('should logout successfully after login', () => {
    cy.visit(loginData.paths.login);

    login(loginData.validUser);

    cy.location('pathname')
      .should('eq', loginData.paths.success);

    logout();

    cy.location('pathname')
      .should('eq', loginData.paths.login);
  });
});
