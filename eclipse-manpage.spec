%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/man

Name:           eclipse-manpage
Version:        0.0.1
Release:        0.svn24060.1.1
Summary:        Man page viewer

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/projectPages/manpage/
## sh %{name}-fetch-src.sh
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: eclipse-pde >= 0:3.4.0
Requires: eclipse-platform >= 3.4.0

%description
Plugin providing common interface for displaying a man page in a view or 
fetching its content for embedded display purposes (e.g hover help).

%prep
%setup -q 

JARS=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
JARS="$JARS $j"
fi
done
if [ ! -z "$JARS" ] ; then
echo "These JARs should be deleted and symlinked to system JARs: $JARS"
exit 1
fi


%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.linuxtools.man

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.man.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.man-feature/license.html
%doc org.eclipse.linuxtools.man-feature/epl-v10.html

