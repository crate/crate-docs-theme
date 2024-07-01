/**
 * GitHub feedback component: Rating, issues, and links to files.
**/
function renderIssues() {

    function makeIssueHeader(open, closed) {
      var html = "<div class='cr-docs-feedback-nav'><ul> \
      <li><a id='issues-open' class='cr-fb-link cr-fb-active' title='View Open issues'>Open (";

                // if more than 30 issues, add "Last"
                if (open.length >= 30) { html += `Last `; }
                html += open.length + ")</a></li> \
                <li><a id='issues-closed' class='cr-fb-link' title='View Closed issues'>Closed (";
                if (closed.length >= 30) { html += `Last `; }
                html += closed.length + ")</a></li> \
                </ul></div>";

                return html;
    }

    function listIssues(issues, isClosed) {
      var divId;
      var display;
      if (!isClosed) {
        divId = "cr-docs-issues-open-list";
        display = 'block';
      } else {
        divId = "cr-docs-issues-closed-list";
        display = 'none';
      }
      var html = `<div style='display: ${display};' id='${divId}' class='cr-docs-feedback-issues'><ul>`;

      // if no issues are found, post this
      if (issues.length == 0) { html += `<li>Currently there is no feedback for this document.</li>` }

        else {
          issues.forEach((issue) => {
            html += `<li><div class='cr-docs-feedback-entry'><div class='cr-docs-feedback-title'><strong><a href='${issue.html_url}' rel='noopener' class='cr-docs-link' title='View issue on GitHub' target='blank'>${issue.title}</a></strong></div>`;

              // show PR if applicable
              if (issue.pull_request != undefined) {
                html += `<div class='cr-docs-feedback-pr'><svg viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true'><path fill-rule='evenodd' d='M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z'><title>Pull Request</title></path></svg></div>`;
              }
              // show # of comments
              if (issue.comments != 0) {
                html += `<div class='cr-docs-feedback-comments'><a href='${issue.html_url}' rel='noopener' class='cr-docs-link' title='View issue on GitHub' target='blank'><svg viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true'><path fill-rule='evenodd' d='M14 1H2c-.55 0-1 .45-1 1v8c0 .55.45 1 1 1h2v3.5L7.5 11H14c.55 0 1-.45 1-1V2c0-.55-.45-1-1-1zm0 9H7l-2 2v-2H2V2h12v8z'><title>Comment</title></path></svg> ${issue.comments}</a></div>`;
              }
              // show issue number + link to it
              html += `</div><div class='cr-docs-feedback-details'><a href='${issue.html_url}' rel='noopener' class='cr-docs-link' title='View issue on GitHub' target='blank'>#${issue.number}</a> `;

              var date = new Date(issue.created_at);

              const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
              var formatted_date = date.getDate() + " "
              + months[date.getMonth()] + " "
              + date.getFullYear();

              html += `opened on ${formatted_date} by <a href='${issue.user.html_url}' rel='noopener' class='cr-docs-link' title='View ${issue.user.login} on GitHub' `;
              html += ` target='blank'>${issue.user.login}</a></br>`;
              html += "</div></li>";
            });
        }

        html += "</ul></div>";
        return html;
      }

      async function fetchIssues(url) {
        const data = await fetch(url).then((response) => response.json());
        return data;
      }

      const content = document.getElementById('cr-feedback-content');
      content.innerHTML = '<p>Loading data...</p>';
      fetchIssues("https://api.{{ github_host|default('github.com') }}/search/issues?q=repo:{{ github_user }}/{{ github_repo }}+label%3A\"area%3A+docs\"+\"{{ title|striptags|urlencode }}\"+\"{{ pagename|urlencode }}.html\"")
          .then(function (issues) {
            const openIssues = issues.items.filter(x => x.state == 'open');
            const closedIssues = issues.items.filter(x => x.state == 'closed');
            var html = makeIssueHeader(openIssues, closedIssues);
            html += listIssues(openIssues);
            html += listIssues(closedIssues, true);
            content.innerHTML = html;
            const openButton = document.getElementById('issues-open');
            const closedButton = document.getElementById('issues-closed');
            const openList = document.getElementById('cr-docs-issues-open-list');
            const closedList = document.getElementById('cr-docs-issues-closed-list');
            openButton.addEventListener('click', function (e) {
              openButton.classList.add('cr-fb-active');
              closedButton.classList.remove('cr-fb-active');
              openList.style.display = 'block';
              closedList.style.display = 'none';
            });
            closedButton.addEventListener('click', function (e) {
              openButton.classList.remove('cr-fb-active');
              closedButton.classList.add('cr-fb-active');
              openList.style.display = 'none';
              closedList.style.display = 'block';
            });
          }).catch(function() {
          // if rate limit exceeded, throw this error
          content.innerHTML = '<p>Error loading data, limit exceeded. Please try again later.</p>';
    });
}
