
// Login before all test
beforeEach(() => {
  cy.visit('http://ec2-3-120-40-183.eu-central-1.compute.amazonaws.com');
  cy.get('[routerlink="login"]').eq(1).click({ multiple: true });
  cy.get('#userName').type('Alysha.Hahn98');
  cy.get('#password').type('Potter3@$!%*?&(){}_');
  cy.get('#loginButton').click();
});

//
describe('Make post', () => {
  it('passes', () => {
    



  })
})