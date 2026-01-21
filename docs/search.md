FOR EDU ONLY!!!

You'll need: apktool, android studio, jdk

# Unpack

```batch
java -jar apktool_2.12.1.jar d wb-my-device.apk -o out_full_decomp
```

edit out_full_decomp/res/xml/network_security_config.xml
add after <network-security-config>:
```xml
<base-config cleartextTrafficPermitted="false">
	<trust-anchors>
		<certificates src="system" />
		<certificates src="user" />
	</trust-anchors>
</base-config>
```

# Create key for sign (once)

```batch
keytool -genkey -v -keystore mykey.keystore -alias myalias -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore mykey.keystore modified.apk myalias
```

# Pack

```batch
java -jar apktool_2.12.1.jar b out_full_decomp/ -o hacked.apk

zipalign -v 4 hacked.apk hacked_aligned.apk
apksigner sign --ks mykey.keystore --ks-key-alias myalias --out hacked_final.apk hacked_aligned.apk
```

# Done
