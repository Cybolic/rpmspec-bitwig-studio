# Build the Bitwig RPM package locally

Make sure your system has the necessary packages in order to build the RPM package:

```bash
sudo dnf install rpm-build rpmdevtools
```

Fetch the source package for Bitwig (the Debian package from their website):

```bash
spectool --get-files --sourcedir ./bitwig-studio.spec
```

Build the RPM package:

```bash
rpmbuild -bb bitwig-studio.spec
```

# Install Bitwig

Install the package (there are simpler ways, but this one selects the version just built):

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/bitwig-studio-$(cat ./bitwig-studio.spec | grep Version | rev | cut -d\  -f1 | rev)-*.rpm
```