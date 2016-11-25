Name     : jdk-google
Version  : 1
Release  : 3
URL      : https://repo.maven.apache.org/maven2/com/google/google/1/google-1.pom
Source0  : https://repo.maven.apache.org/maven2/com/google/google/1/google-1.pom
Source1  : https://repo.maven.apache.org/maven2/com/google/google/1/google-1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/google.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/google.xml \
%{buildroot}/usr/share/maven-poms/google.pom \
%{buildroot}/usr/share/java/google.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/google.xml
/usr/share/maven-poms/google.pom
