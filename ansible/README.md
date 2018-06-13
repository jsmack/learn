# TOC
<!-- TOC -->

- [TOC](#toc)
    - [readme](#readme)
        - [ansible-vault](#ansible-vault)

<!-- /TOC -->

---

## readme
### ansible-vault

```
- private.yml
    - vault_password.test_password 
- public.yml
    - pass {{ vault_password.test_password }}
- site.yml
    - {{ pass }}
```

- encrypt 

```
testuser@elemently:~/nfs/ansible/vault$ cat private.yml
---
password: 'hogefuga'
testuser@elemently:~/nfs/ansible/vault$
testuser@elemently:~/nf   s/ansible/vault$ ansible-vault encrypt private.yml
New Vault password:
Confirm New Vault password:
Encryption successful
testuser@elemently:~/nfs/ansible/vault$
testuser@elemently:~/nfs/ansible/vault$ cat private.yml
$ANSIBLE_VAULT;1.1;AES256
62366465383734363561383463346532356432356665393930316530356435373936666139363635
6431633539356138376262633238633563306239373663360a663261386464373263643939663335
30643761333331306664386534616366306562363832383866346535326365663365643832333564
6464663437646465310a386664313133353133623734386337303231336532366466613933613865
36373232653238356430616132383336356337633036343764323433616234306232
testuser@elemently:~/nfs/ansible/vault$
```

- encrypt check

```
testuser@elemently:~/nfs/ansible/vault$ cat private.yml
---
password: 'hogefuga'
testuser@elemently:~/nfs/ansible/vault$
testuser@elemently:~/nfs/ansible/vault$ ansible-vault encrypt private.yml
New Vault password:
Confirm New Vault password:
Encryption successful
testuser@elemently:~/nfs/ansible/vault$
testuser@elemently:~/nfs/ansible/vault$ cat private.yml
$ANSIBLE_VAULT;1.1;AES256
62366465383734363561383463346532356432356665393930316530356435373936666139363635
6431633539356138376262633238633563306239373663360a663261386464373263643939663335
30643761333331306664386534616366306562363832383866346535326365663365643832333564
6464663437646465310a386664313133353133623734386337303231336532366466613933613865
36373232653238356430616132383336356337633036343764323433616234306232
testuser@elemently:~/nfs/ansible/vault$
```
- encrypt edit
```
testuser@elemently:~/nfs/ansible/vault$ ansible-vault edit private.yml
Vault password:
testuser@elemently:~/nfs/ansible/vault$
testuser@elemently:~/nfs/ansible/vault$ ansible-vault view private.yml
Vault password:
---
password: 'nyan'
testuser@elemently:~/nfs/ansible/vault$
```

- decrypt
```
testuser@elemently:~/nfs/ansible/vault$ cat private.yml
---
password: 'nyan'
testuser@elemently:~/nfs/ansible/vault$
```

- run error

```
testuser@elemently:~/nfs/ansible/vault$ ansible-playbook -i hosts site.yml
ERROR! Attempting to decrypt but no vault secrets found
testuser@elemently:~/nfs/ansible/vault
```

- run (succeed)
    - add `--ask-vault-pass` argument
```
testuser@elemently:~/nfs/ansible/vault$ ansible-playbook -i hosts site.yml  --ask-vault-pass
Vault password:

PLAY [localhost] ****************************************************************************************************************************************************************************************************************************************

TASK [debug] ********************************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "passwd  nyan "
}

PLAY RECAP **********************************************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0

testuser@elemently:~/nfs/ansible/vault$
```
