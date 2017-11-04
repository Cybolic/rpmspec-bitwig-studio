Name:           bitwig-studio
Version:        2.2.2
Release:        1%{?dist}
Summary:        A dynamic software for creation and performance of your musical ideas on stage or in the studio.

License:        EULA
URL:            https://www.bitwig.com/
Source0:        https://www.bitwig.com/dl/stable/%{version}/%{name}-%{version}.deb
Source1:        http://security.ubuntu.com/ubuntu/pool/universe/f/ffmpeg/libavcodec-ffmpeg-extra56_2.8.11-0ubuntu0.16.04.1_amd64.deb
Source2:        http://security.ubuntu.com/ubuntu/pool/universe/f/ffmpeg/libavformat-ffmpeg56_2.8.11-0ubuntu0.16.04.1_amd64.deb

BuildRequires:  dpkg
Requires:       xcb-util-wm, bzip2-libs >= 1.0, bzip2-libs < 2.0


%global __requires_exclude_from ^(/opt/bitwig-studio/bin/.*\\.so.*|/opt/bitwig-studio/bin/jre/lib/amd64/headless/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/jli/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/server/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/xawt/.*\\.so|/opt/bitwig-studio/bin/vamp-plugins/.*\\.so)$
%global _privatelibs libav(codec|format).*[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$


%description 
Bitwig Studio is a dynamic software for creation and performance of your musical ideas on stage or in the studio.

Discover the new standard in customized workflow. Bitwig Studio inspires you to take greater control of your music,
giving you access to every aspect of your production. Streamline your creative process and quickly evolve your ideas
into complete songs, tracks and compositions. Record and arrange, improvise and perform, or do it all at once.

Bitwig Studio comes loaded with industry-standard to industry-leading features, designed to meet the demands of
present day musicians, producers and sound designers.

Welcome to the next generation of music creation and performance software for Windows, Mac OS X, and Linux.
 

%prep
# Unpack Bitwig deb package
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
dpkg -x %{SOURCE0} $RPM_BUILD_DIR/%{name}-%{version}
# Unpack libavcodec-ffmpeg-extra56 deb package
cd $RPM_BUILD_DIR
mkdir -p %{name}-%{version}libavcodec-ffmpeg-extra56
dpkg -x %{SOURCE1} $RPM_BUILD_DIR/%{name}-%{version}/libavcodec-ffmpeg-extra56
# Unpack libavformat-ffmpeg56 deb package
cd $RPM_BUILD_DIR
mkdir -p %{name}-%{version}libavformat-ffmpeg56
dpkg -x %{SOURCE2} $RPM_BUILD_DIR/%{name}-%{version}/libavformat-ffmpeg56


%install
# Move the Bitwig install files to the build root
mv $RPM_BUILD_DIR/%{name}-%{version}/{opt,usr} %{buildroot}/

# Add libavcodec-ffmpeg.so.56 from Ubuntu 16.04 LTS to the Bitwig static libraries
mv $RPM_BUILD_DIR/%{name}-%{version}/libavcodec-ffmpeg-extra56/usr/lib/x86_64-linux-gnu/libavcodec-ffmpeg.so.56* %{buildroot}/opt/bitwig-studio/lib/bitwig-studio/

# Add libavformat-ffmpeg.so.56 from Ubuntu 16.04 LTS to the Bitwig static libraries
mv $RPM_BUILD_DIR/%{name}-%{version}/libavformat-ffmpeg56/usr/lib/x86_64-linux-gnu/libavformat-ffmpeg.so.56* %{buildroot}/opt/bitwig-studio/lib/bitwig-studio/

# Alias libbz2.so.1 to the filename Bitwig expects to find
ln -s /usr/lib64/libbz2.so.1 %{buildroot}/opt/bitwig-studio/lib/bitwig-studio/libbz2.so.1.0



%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
/opt/bitwig-studio
/usr/bin/bitwig-studio
/usr/share/applications/bitwig-studio.desktop
/usr/share/icons/hicolor/48x48/apps/bitwig-modular.png
/usr/share/icons/hicolor/48x48/apps/bitwig-studio.png
/usr/share/icons/hicolor/scalable/apps/bitwig-modular.svg
/usr/share/icons/hicolor/scalable/apps/bitwig-studio.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-bitwig-clip.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-bitwig-device.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-bitwig-preset.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-bitwig-project.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-bitwig-project-folder.svg
/usr/share/mime/packages/bitwig-studio.xml


%changelog
* Sat Nov 4 2017 Christian Dannie Storgaard <cybolic@gmail.com> - 2.2.2-1
- First version