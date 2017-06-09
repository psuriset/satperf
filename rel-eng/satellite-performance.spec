Name:          satellite-performance
Version:       master
Release:       1%{?dist}
Summary:       Red Hat Satellite 6 Performance testing framework and tests
License:       GPLv2
Group:         Development/Tools
URL:           https://github.com/redhat-performance/satellite-performance
Source0:       https://github.com/redhat-performance/satellite-performance/archive/%{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch
Requires:      ansible


%description
Red Hat Satellite 6 Performance testing framework and tests


%prep
%setup -qc
pwd
ls -al


%build


%install
rm -rf %{buildroot}
pushd %{name}-%{version}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp README.md %{buildroot}/%{_datadir}/%{name}
cp LICENSE %{buildroot}/%{_datadir}/%{name}
cp cleanup %{buildroot}/%{_datadir}/%{name}
cp ansible.cfg %{buildroot}/%{_datadir}/%{name}
cp -r playbooks %{buildroot}/%{_datadir}/%{name}
mkdir %{buildroot}/%{_datadir}/%{name}/conf
cp conf/hosts.ini %{buildroot}/%{_datadir}/%{name}/conf
cp conf/satperf.yaml %{buildroot}/%{_datadir}/%{name}/conf
popd


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}


%changelog
* Wed May 31 2017 Jan Hutar <jhutar@redhat.com> 1.1-1
- Init
