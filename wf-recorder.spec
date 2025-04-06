%global commit 779a61881273852ed7ea34b0639727d17db07266
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		wf-recorder
Version:	1~git%{shortcommit}
Release:	1
Source0:	https://github.com/ammen99/wf-recorder/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:   wf-recorder-use-free-codecs.patch
Summary:	Screen recorder for wlroots-based compositors eg swaywm
URL:		https://github.com/ammen99/wf-recorder
License:	MIT
Group:		Window Manager/utility

BuildSystem:    meson

BuildRequires: pkgconfig(OpenCL)
BuildRequires: pkgconfig(gbm)
BuildRequires: libavutil
BuildRequires: libavcodec
BuildRequires: libpulseaudio-devel
BuildRequires: ffmpeg-devel
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpipewire-0.3) >= 1.0.5
BuildRequires: pkgconfig(wayland-client) >= 1.20
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: scdoc

%description
wf-recorder is a utility program for screen recording of wlroots-based
compositors (more specifically, those that support wlr-screencopy-v1
and xdg-output).

%prep
%autosetup -n %{name}-%{commit} -p1

%files
%{_bindir}/wf-recorder*
%{_datadir}/fish/fish/vendor_completions.d/wf-recorder.fish
%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE
