# Security and sensitive material

Do not commit access tokens, passwords, private keys, unpublished personal information, or credentials for connected hardware/services. Use local environment variables when implementation begins, and commit only sanitized examples.

For a suspected exposed secret, avoid posting the value in a public issue. Use the repository's private vulnerability reporting feature if it is enabled, or contact the repository owner through an agreed private channel. Revoke/rotate a confirmed exposed credential promptly; deleting the current file alone does not remove it from Git history.

General documentation defects and non-sensitive engineering issues can be filed through the issue templates. Hardware risks should include the affected configuration and evidence; do not represent repository CI as a safety certification.

There is currently no deployed software or supported binary release in this repository.
