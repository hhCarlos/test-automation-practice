import { loginSelectors } from './login.selectors';

export const fillLoginForm = ({ username, password }) => {
  cy.get(loginSelectors.form.usernameInput)
    .clear()
    .type(username);

  cy.get(loginSelectors.form.passwordInput)
    .clear()
    .type(password);
};

export const submitLoginForm = () => {
  cy.get(loginSelectors.form.submitButton)
    .click();
};

export const login = (credentials) => {
  fillLoginForm(credentials);
  submitLoginForm();
};

export const logout = () => {
  cy.get(loginSelectors.success.logoutButton)
    .should('be.visible')
    .click();
};
