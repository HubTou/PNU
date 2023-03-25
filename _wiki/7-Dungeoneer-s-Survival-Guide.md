# [Dungeoneer's Survival Guide](https://en.wikipedia.org/wiki/Dungeoneer%27s_Survival_Guide)
This place is dedicated to documenting security issues in The PNU Project.

Each command is scanned with the [bandit](https://pypi.org/project/bandit/) tool. 

## Unmitigated issues
None

## All issues (detailed)

### [b2bt(1)](https://github.com/HubTou/b2bt)
* [Security considerations](https://github.com/HubTou/b2bt#security-considerations) in the [manual page](https://github.com/HubTou/b2bt/blob/main/README.md).
  * The command is perfectly safe for your own use or with The PNU project [test files](https://github.com/HubTou/PNU/tree/main/tests).
  * For test files from unknown sources, make sure to:
    * review those files prior to execution,
    * use the b2bt command with an unpriviledged account (builtin warning)
    * use the b2bt command with autoconfirmation option disabled (default behaviour)

* [Bandit output](https://github.com/HubTou/b2bt/blob/main/misc/bandit.txt). Details:

Issue|Severity|Status
---|---|---
[[B404:blacklist]](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b404-import-subprocess) Consider possible security implications associated with subprocess module|:large_orange_diamond: Low|:heavy_check_mark: OK
[[B303:blacklist]](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b303-md5) Use of insecure MD2, MD4, MD5, or SHA1 hash function|:small_orange_diamond: Medium|:heavy_check_mark: OK
[[B607:start_process_with_partial_path]](https://bandit.readthedocs.io/en/latest/plugins/b607_start_process_with_partial_path.html) Starting a process with a partial executable path|:small_orange_diamond: Low|:white_check_mark: Mitigated 
[[B603:subprocess_without_shell_equals_true]](https://bandit.readthedocs.io/en/latest/plugins/b603_subprocess_without_shell_equals_true.html) subprocess call - check for execution of untrusted input|:small_orange_diamond: Low|:heavy_check_mark: OK
[[B602:subprocess_popen_with_shell_equals_true]](https://bandit.readthedocs.io/en/latest/plugins/b602_subprocess_popen_with_shell_equals_true.html) subprocess call with shell=True identified, security issue|:red_circle: High|:white_check_mark: Mitigated

