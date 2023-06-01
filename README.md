# Windows-Admin-Remover

A python script for removing users from `Administrators` local group and adding them to `Users` local group in Windows.

This is generally useful for organizations or individuals who want to remove admin privileges from their provided laptops to their employees.

## Usage

1. Run the `Command prompt` as an administrator in your Windows machine.

2. Clone the repository: 

    ```bash
     git clone https://github.com/manavarya999/windows-admin-remover.git
    ```

3. Head over to the directory: 

    ```bash
     cd windows-admin-remover
    ``` 
4. Run the python script:

    ```bash
     python windows-admin-remover.py
    ```
5. To check that the user has been removed from `Administrators` group and added to `Users` group, execute the following command:

    ```bash
     net user <username>
    ```
6. Look under `Local Group Memberships` it should be equivalent to `*Users` only.
