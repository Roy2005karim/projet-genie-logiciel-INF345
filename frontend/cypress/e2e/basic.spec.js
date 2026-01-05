describe('Basic E2E', () => {
  it('loads the frontend', () => {
    cy.visit('http://localhost:3000');
    cy.contains('RestoQuick');
  });
});
