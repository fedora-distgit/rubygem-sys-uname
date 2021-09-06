# Generated from sys-uname-1.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sys-uname

Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 1%{?dist}
Summary: An interface for returning uname (platform) information
License: Apache-2.0
URL: http://github.com/djberg96/sys-uname
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
The sys-uname library provides an interface for gathering information
about your current platform. The library is named after the Unix 'uname'
command but also works on MS Windows. Available information includes
OS name, OS version, system name and so on. Additional information is
available for certain platforms.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/CHANGES.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MANIFEST.md
%{gem_instdir}/certs
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/spec
%{gem_instdir}/sys-uname.gemspec

%changelog
* Mon Sep 06 2021 Pavel Valena <pvalena@redhat.com> - 1.2.2-1
- Initial package
