/**
 * Keyboard navigation for GitHub. CTRL+G will navigate to
 * the edit page on GitHub for the corresponding document.
**/
document.addEventListener('keydown', (event) => {
  if (event.key === 'g' && event.ctrlKey) {
    {% if check_meta and 'github_url' in meta %}
      location.href = "{{ meta['github_url'] }}";
    {% else %}
      location.href = "https://{{ github_host|default('github.com') }}/{{ github_user }}/{{ github_repo }}/{{ theme_vcs_pageview_mode|default('edit') }}/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}";
    {% endif %}
  }
});
