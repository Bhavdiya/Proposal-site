from flask import Flask, render_template, request, redirect, url_for
import secrets

app = Flask(__name__)


proposals = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create', methods=['GET', 'POST'])
def create_proposal():
    if request.method == 'POST':
        proposer_name = request.form['proposer_name']
        partner_name = request.form['partner_name']
        message = request.form['message']
        unique_link = secrets.token_urlsafe(12)

        proposals[unique_link] = {
            'proposer_name': proposer_name,
            'partner_name': partner_name,
            'message': message
        }

        return redirect(url_for('proposal_link', link=unique_link))
    return render_template('create.html')


@app.route('/proposal/<link>')
def view_proposal(link):
    proposal = proposals.get(link)
    if proposal:
        return render_template('proposal.html', proposal=proposal)
    return "Proposal not found", 404


@app.route('/link/<link>')
def proposal_link(link):
    return render_template('link.html', link=link)


if __name__ == '__main__':
    app.run(debug=True)
