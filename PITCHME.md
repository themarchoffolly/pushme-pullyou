
```
public class Main implements SauceOnDemandSessionIdProvider {
  final private String USERNAME = System.getenv("SAUCE_USERNAME");
  final private String ACCESS_KEY = System.getenv("SAUCE_ACCESS_KEY");
  private SauceOnDemandAuthentication authentication = new SauceOnDemandAuthentication(USERNAME, ACCESS_KEY);

  private IOSDriver driver;
  private String sessionId;

  @Rule
  public SauceOnDemandTestWatcher resultReportingTestWatcher = new SauceOnDemandTestWatcher(this, authentication);
  @Override
  public String getSessionId() {
    return sessionId;
  }

public @Rule TestName name = new TestName();
```

@[1](Line 1)
@[2,3,4](Lines 2,3,4)
@[2,3,4, 6-7](Lines 2,3,4, 6-7)
@[6-7, 9-14](Lines 6-7, 9-14)
@[1, 16](Lines 1, 16)
